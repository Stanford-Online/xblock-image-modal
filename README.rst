Image Modal XBlock
==================
A fullscreen image modal XBlock.

This package is meant to be installed within the OpenEdX platform.

Installation, system administrator
--------------------

To install the XBlock on your platform,
add the following to your `requirements.txt` file:

    xblock-image-modal

You'll also need to add this to your `INSTALLED_APPS`:

    imagemodal


Installation, course staff
--------------------

To install the XBlock in your course,
add the following to your `ADVANCED_COMPONENTS` (?) list:

    imagemodal



''.join([word.capitalize() for word in sentence.lower().replace('xblock', '').replace('-', ' ').replace('_', ' ').split(' ')])

{{ sentence|lower|replace('xblock', '')|replace('-', ' ')|replace('_', ' ')|title }}
