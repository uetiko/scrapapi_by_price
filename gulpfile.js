var gulp = require("gulp");
var watch = require("gulp-watch");
var ts = require('gulp-typescript');
var tsProject = ts.createProject('tsconfig.json');

gulp.task("default", function(){
  return tsProject.src().pipe(tsProject()).js.pipe(gulp.dest("static/js/"));
});
gulp.task('watch', ["default"], function() {
    gulp.watch('src/*.ts', ["default"]);
});
