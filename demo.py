import yaml

with open('config/config.yaml') as f:
    data = yaml.safe_load(f)

print(data["kitti_data"])