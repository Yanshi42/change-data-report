"""Verify the published report manifest and stage only declared static files."""
import hashlib
import json
from pathlib import Path
import shutil

root=Path(__file__).resolve().parents[2]
destination=root/'_site'
manifest=json.loads((root/'manifest.json').read_text())
assert not destination.exists(), 'Output folder already exists'
for item in manifest['files']:
    relative=Path(item['path'])
    assert not relative.is_absolute() and '..' not in relative.parts
    source=root/relative
    assert source.is_file() and not source.is_symlink(),relative
    assert source.stat().st_size==item['bytes'],relative
    assert hashlib.sha256(source.read_bytes()).hexdigest()==item['sha256'],relative
    target=destination/relative
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(source,target)
shutil.copyfile(root/'manifest.json',destination/'manifest.json')
assert 'data-initial-view="catalog"' in (destination/'index.html').read_text()
data=json.loads((destination/'data/report-data.json').read_text())
assert len(data['catalog_categories'])==80 and len(data['products'])==238
for product in data['products']:
    for image in product['images']:
        assert (destination/image['src']).is_file() and (destination/image['thumb']).is_file()
    for table in product['tables']:
        assert (destination/table['src']).is_file()
print(f'Verified {len(manifest["files"])} files; 80 categories; 238 products.')
