# {%= title %}
{%= description %}

## TODO List:
- [ ] Write tests
- [ ] Update the `student_view`
    - [ ] `./{%= namePackage %}/private/view.html`
        - Add content to `<div class="{%= namePackage %}_block"></div>` element
    - [ ] `./{%= namePackage %}/private/view.js`
        - Add logic to `{%= nameClass %}View` function
    - [ ] `./{%= namePackage %}/private/view.less`
        - Add styles to `.{%= namePackage %}_block { }` block
    - [ ] `./{%= namePackage %}/{%= namePackage %}.py`
        - Add back-end logic to `student_view` method
- [ ] Update the `studio_view`
    - [ ] `./{%= namePackage %}/private/edit.html`
        - Add `<LI>` entries to `<ul class="list-input settings-list">` for each new field
    - [ ] `./{%= namePackage %}/private/edit.js`
        - Add entry for each field to `{%= nameClass %}Edit
    - [ ] `./{%= namePackage %}/private/edit.less`
        - Add styles to `.{%= namePackage %}_edit { }` block (if needed)
    - [ ] `./{%= namePackage %}/{%= namePackage %}.py`
        - Add entry for each field to `{%= studio_view_save %}`
- [ ] Update package metadata
    - [ ] `./package.json`
        - https://www.npmjs.org/doc/files/package.json.html
    - [ ] `./setup.py`
        - https://docs.python.org/2/distutils/setupscript.html#additional-meta-data
- [ ] Update `./Gruntfile.js`
    - http://gruntjs.com/getting-started
- [ ] Update `./README.markdown`
- [ ] Write documentation
- [ ] Publish on PyPi
