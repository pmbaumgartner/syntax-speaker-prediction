### Notes on Data Creation

- False Start: Not an HTML annotation, but need to write HTML for choices view
- syntax081-0764.mp3 - "its not working"
- chrome://flags/#autoplay-policy
- https://developers.google.com/web/updates/2017/09/autoplay-policy-changes


### Serve MP3s

`$ cd syntax-clips && python -m http.server 9999`

Help: - https://support.prodi.gy/t/working-with-languages-not-yet-supported-by-spacy/206/17
- https://stackoverflow.com/questions/39007243/cannot-open-local-file-chrome-not-allowed-to-load-local-resource


### Create Recipe

https://prodi.gy/docs/workflow-custom-recipes#example-choice

### Prodigy Settings

`prodigy.json`
```javascript
{
    ...
    "show_stats": true,
    "choice_auto_accept": true,
    ...
}
```

### Prodigy Start

```bash
$ prodigy dataset syntax-label "Syntax Speaker Labels"
$ prodigy audio-choice syntax-label prodigy-json/044.jsonl -F recipe.py
```


### Export
https://prodi.gy/docs/recipes#db-out

`$ prodigy db-out syntax-label output`
(output is a directory, the file name will be the dataset name)