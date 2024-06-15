Dataset **FIRE** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](/supervisely-supervisely-assets-public/teams_storage/4/a/X6/4ewrOqOQkVvPjM4W64TbcM7JsSgnqnGIhj91gvntLmNKE1wEvwLyPbG162lJ8f1phm9vXCO2IpQmhM7JuGDHQzgpcGoFuHOHF3zSlyuPggWb0bATymNMAHv1y9EM.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='FIRE', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://projects.ics.forth.gr/cvrl/fire/FIRE.7z).