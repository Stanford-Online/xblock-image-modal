# Image Modal XBlock
A fullscreen image modal XBlock.

## TODO List:
- [ ] Write tests
- [ ] Update the `student_view`
    - [ ] `./imagemodal/private/view.html`
        - Add content to `<div class="imagemodal_block"></div>` element
    - [ ] `./imagemodal/private/view.js`
        - Add logic to `ImageModalView` function
    - [ ] `./imagemodal/private/view.less`
        - Add styles to `.imagemodal_block { }` block
    - [ ] `./imagemodal/imagemodal.py`
        - Add back-end logic to `student_view` method
- [ ] Update the `studio_view`
    - [ ] `./imagemodal/private/edit.html`
        - Add `<LI>` entries to `<ul class="list-input settings-list">` for each new field
    - [ ] `./imagemodal/private/edit.js`
        - Add entry for each field to `ImageModalEdit
    - [ ] `./imagemodal/private/edit.less`
        - Add styles to `.imagemodal_edit { }` block (if needed)
    - [ ] `./imagemodal/imagemodal.py`
        - Add entry for each field to ``
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
