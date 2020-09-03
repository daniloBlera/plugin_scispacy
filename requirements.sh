#!/bin/sh
echo 'Installing ScispaCy...'
pip install -U scispacy
echo 'Done installing ScispaCy'

echo 'Downloading the basic biomedica model...'
pip install 'https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_core_sci_sm-0.2.5.tar.gz'
echo 'Done downloading the model'
