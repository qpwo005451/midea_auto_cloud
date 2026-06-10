# Deployed v0.3.3 Delta Capture

This artifact bundle preserves the exact deployed local customizations that were copied from the live Home Assistant `midea_auto_cloud` integration, without editing `custom_components/midea_auto_cloud/` in this repo.

## Preserved live files

- `live/custom_components/midea_auto_cloud/device_mapping/T0xD9.py`
- `live/custom_components/midea_auto_cloud/device_mapping/T0xD9.py.bak`
- `live/custom_components/midea_auto_cloud/translations/en.json`
- `live/custom_components/midea_auto_cloud/translations/zh-Hans.json`

## Files that differ from upstream `v0.3.3`

- `device_mapping/T0xD9.py`: expands D9 support with a `dc` query path, dryer-side `dc_*` switch/select/sensor/number entities, wash-dry link control, and appointment-related entities.
- `translations/en.json`: adds English names and states for the deployed D9 washer/dryer entities and keeps the deployed wording overrides that ship with the live customization.
- `translations/zh-Hans.json`: adds Simplified Chinese names and states for the same D9 washer/dryer entities and keeps the deployed wording overrides from the live customization.
- `device_mapping/T0xD9.py.bak`: extra deployed backup file. Its line content matches upstream `v0.3.3` `T0xD9.py`; the live copy is preserved as-is from the deployment.

## Customized functional areas

- D9 washer and dryer dual-bucket entity exposure
- Dryer program, dry-time, temperature-level, and deodorize-time selections
- Washer/dryer appointment toggles, durations, and end-time sensors
- Washer/dryer localization strings for the added controls and status entities

## Patch production

The patch at `patches/upstream-v0.3.3-to-deployed.patch` was produced from actual file contents, not from the current branch source tree:

1. Copy the live deployed files into `live/custom_components/midea_auto_cloud/...`.
2. Run `python artifacts/deployed-v0.3.3-delta/scripts/build_patch.py` from the repo root.
3. The script exports upstream `v0.3.3` blobs with `git show`, stages them beside the preserved live copies in a temporary directory, and runs `git diff --no-index`.
4. The saved patch normalizes the diff labels to `a/custom_components/...` and `b/custom_components/...` for readability.
