import gulp from 'gulp'
import gutil from 'gulp-util'
import livereload from 'gulp-livereload'

import newer from 'gulp-newer'
import clean from 'gulp-clean'

import less from 'gulp-less'
import autoprefixer from 'gulp-autoprefixer'
import sourcemaps from 'gulp-sourcemaps'
import minifyCSS from 'gulp-minify-css'

import source from 'vinyl-source-stream'
import buffer from 'vinyl-buffer'
import browserify from 'browserify'
import babelify from 'babelify'
import uglify from 'gulp-uglify'

const
    dirs = {
        vendor: './node_modules',
        src: './frontend',
        semantic: './frontend/semantic',
        dest: './marketplace/static'
    },
    files = {
        vendor: {
            jquery: `${dirs.vendor}/jquery/dist/jquery.min.js`,
            fancybox: `${dirs.vendor}/fancybox/dist/**/*.*`
        },
        semantic: {
            js: `${dirs.semantic}/dist/semantic.min.js`,
            css: `${dirs.semantic}/dist/semantic.min.css`,
            theme: `${dirs.semantic}/dist/themes/default/**/*.*`
        },
        source: {
            script: `${dirs.src}/scripts/script.js`,
            style_dir: `${dirs.src}/less/`,
            style: `${dirs.src}/less/style.less`
        },
        dest: {
            vendor: `${dirs.dest}/vendor`,
            fancybox: `${dirs.dest}/vendor/fancybox`,
            semantic: `${dirs.dest}/vendor/semantic`,
            semantic_theme: `${dirs.dest}/vendor/semantic/themes/default/`,
            scripts: `${dirs.dest}/scripts`,
            styles: `${dirs.dest}/styles`
        }
    };


gulp.task('clean', () => {
    for(let i of Object.keys(files.dest)){
        gulp.src(files.dest[i], {read: false}).pipe(clean());
    }
});


gulp.task('copy', () => {
    gulp.src(files.vendor.jquery)
        .pipe(newer(`${files.dest.vendor}/jquery.min.js`))
        .pipe(gulp.dest(files.dest.vendor));
    gulp.src(files.vendor.fancybox)
        .pipe(gulp.dest(files.dest.fancybox));
    gulp.src(files.semantic.js)
        .pipe(newer(`${files.dest.semantic}/semantic.min.js`))
        .pipe(gulp.dest(files.dest.semantic));
    gulp.src(files.semantic.css)
        .pipe(newer(`${files.dest.semantic}/semantic.min.css`))
        .pipe(gulp.dest(files.dest.semantic));
    gulp.src(files.semantic.theme)
        .pipe(gulp.dest(files.dest.semantic_theme));
});


gulp.task('less', () => {
    let production = gutil.env.type === 'production';
    return gulp.src(files.source.style)
        .pipe(production ? gutil.noop() : sourcemaps.init())
        .pipe(less())
        .pipe(autoprefixer({
            browsers: ['> 5%', 'last 2 versions'],
            cascade: !production
        }))
        .pipe(production ? minifyCSS() : gutil.noop())
        .pipe(production ? gutil.noop() : sourcemaps.write())
        .pipe(gulp.dest(files.dest.styles));
});


gulp.task('compile', () => {
    let production = gutil.env.type === 'production';
    return browserify(
        {
            entries: files.source.script,
            debug: !production,
            transform: [babelify.configure({
                'presets': ['es2015']
            })]
        }
    )
        .bundle()
        .pipe(source('script.js'))
        .pipe(buffer())
        .pipe(production ? uglify() : gutil.noop())
        .pipe(gulp.dest(files.dest.scripts))
        .pipe(production ? gutil.noop() : livereload());
});


gulp.task('watch', () => {
    livereload.listen();
    gulp.watch(`${dirs.src}/**/*.js`, ['compile']);
    gulp.watch(`${dirs.src}/**/*.less`, ['less']);
});

let task_pool = ['copy', 'less', 'compile'];
if(gutil.env.type !== 'production') {
    task_pool.push('watch');
}


gulp.task('default', task_pool);
