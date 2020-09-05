# plugin_scispacy
A [scispaCy][scispacy] plugin for [DeepNLPF][deepnlpf].

## Installation
To install the scispacy plugin and its dependencies, do:

```zsh
deepnlpf --install_user_plugin 'https://github.com/daniloBlera/plugin_scispacy/archive/master.zip'
```

After installing the plugin's dependencies, download the biomedical models executing

```zsh
pip install MODEL_URL
```

To install the small biomedical model `en_core_sci_sm`, do:

```zsh
pip install 'https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_core_sci_sm-0.2.5.tar.gz'
```

The other available biomedical models can be found here: [https://allenai.github.io/scispacy/][scispacy]

[scispacy]: https://allenai.github.io/scispacy/
[deepnlpf]: https://github.com/deepnlpf/deepnlpf
