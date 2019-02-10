module.exports = function (grunt) {
    'use strict';
    var gruntFile = 'Gruntfile.js';
    var directoryPackage = './imagemodal';
    var directoryPrivate = directoryPackage + '/private';
    var directoryPublic = directoryPackage + '/public';
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        copy: {
            images: {
                files: [
                    {
                        expand: true,
                        src: [
                            directoryPrivate + '/**/*.jpg',
                            directoryPrivate + '/**/*.png',
                            directoryPrivate + '/**/*.gif',
                        ],
                        dest: directoryPublic + '/',
                    },
                ],
            },
        },
    });
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.registerTask('default', [
        'copy',
    ]);
};
