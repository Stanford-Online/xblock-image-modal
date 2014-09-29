module.exports = function (grunt) {
    'use strict';

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        jshint: {
            grunt: [
                './Gruntfile.js',
                './package.json',
                './skel/template.js',
                './skel/root/Gruntfile.js',
            ],
        },
    });

    grunt.loadNpmTasks('grunt-contrib-jshint');

    grunt.registerTask('default', [
        'jshint:grunt',
    ]);
};
