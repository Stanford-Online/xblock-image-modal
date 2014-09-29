exports.template = function template(grunt, init, done) {
    'use strict';

    function getPackageName(name, camelCase) {
        var names;
        name = name || '';
        camelCase = camelCase || false;
        name = name.split('.').join('-');
        name = name.split('_').join('-');
        name = name.split(' ').join('-');
        names = name.split('-');
        if (camelCase) {
            names.forEach(function (item, index, array) {
                array[index] = [
                    item[0].toUpperCase(),
                    item.slice(1),
                ].join('');
            });
        }
        name = names.join('');
        return name;
    }

    grunt = grunt || {};
    init.process({}, [
        init.prompt('name'),
        init.prompt('title'),
        init.prompt('description'),
        init.prompt('version'),
        init.prompt('repository'),
        init.prompt('homepage'),
        init.prompt('bugs'),
        init.prompt('author_name'),
        init.prompt('author_email'),
        init.prompt('author_url'),
        init.prompt('keywords', 'openedx xblock'),
    ], function (error, properties) {
        var path;
        var file;
        var fileNew;
        var files = init.filesToCopy(properties);
        error = error || {};
        properties.namePackage = getPackageName(properties.name);
        properties.nameClass = getPackageName(properties.name, true);

        for (file in files) {
            if (!files.hasOwnProperty(file)) {
                continue;
            }
            path = files[file];
            fileNew = file.split('package').join(properties.namePackage);
            if (file !== fileNew) {
                delete files[file];
                files[fileNew] = path;
            }
        }

        properties.license = 'AGPL-3.0';
        if (properties.keywords) {
            properties.keywords = properties.keywords.split(' ');
        }
        properties.scripts = {
            "test": "grunt --verbose"
        };
        properties.devDependencies = {
            "grunt": "^0.4.5",
            "grunt-contrib-jshint": "^0.10.0",
            "grunt-contrib-concat": "^0.5.0",
            "grunt-contrib-uglify": "^0.6.0",
            "grunt-contrib-less": "^0.11.4",
            "grunt-contrib-csslint": "^0.3.1",
            "grunt-contrib-cssmin": "^0.10.0",
            "grunt-contrib-watch": "^0.6.1",
            "grunt-contrib-copy": "^0.6.0",
            "grunt-contrib-clean": "^0.6.0",
            "grunt-contrib-htmlmin": "^0.3.0",
        };

        init.copyAndProcess(files, properties);
        init.writePackageJSON('package.json', properties);

        done();
    });
};
