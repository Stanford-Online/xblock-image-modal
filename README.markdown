# XBlock Factory

## Setup:
1. [Fork this repo in Github.](https://github.com/Stanford-Online/xblock-factory/fork)
2. Rename your new repo in Github.
3. Clone your repo.
    - `git clone ${YOUR_PROJECT_REPO} ${YOUR_PROJECT_PATH}`
4. Enter your project directory.
    - `cd ${YOUR_PROJECT_PATH}`
5. Run the bootstrap script.
    - `./bootstrap.sh`

## Develop
1. Run the `watch` task.
    - `grunt watch`
2. Edit files.
    - Note: you should only edit static files (HTML, CSS, JS) inside of
      the `private/` directory and _not_ the copies inside `public/`.
    - The `public/` directory is recreated and overwritten automatically
      by `grunt`, which compiles and minifies static content.
    - While `grunt watch` will update files automatically when they
      change, you can manually build/lint your project by invoking the
      build task with `grunt`.
3. ???
4. Profit!
