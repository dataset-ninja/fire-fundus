import os
import shutil

import supervisely as sly
from supervisely.io.fs import (
    file_exists,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s
from dataset_tools.convert import unpack_if_archive


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # Possible structure for bbox case. Feel free to modify as you needs.

    images_path = "/home/alex/DATASETS/IMAGES/FIRE/Images"
    points_path = "/home/alex/DATASETS/IMAGES/FIRE/Ground Truth"

    batch_size = 30
    group_tag_name = "im_id"
    point_prefix = "control_points_"
    point_suffix = "_1_2.txt"

    ds_name = "ds"


    def create_ann(image_path):
        labels = []
        tags = []

        image_name = get_file_name(image_path)

        im_id_value = image_name.split("_")[0]
        group_tag = sly.Tag(group_tag_meta, value=im_id_value)
        tags.append(group_tag)

        # image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = 2912  # image_np.shape[0]
        img_wight = 2912  # image_np.shape[1]

        ann_name = point_prefix + im_id_value + point_suffix
        ann_path = os.path.join(points_path, ann_name)

        with open(ann_path) as f:
            content = f.read().split("\n")

        for curr_point_str in content:
            if len(curr_point_str) != 0:
                points = list(map(float, curr_point_str.split(" ")))
                point_ref = sly.Point(points[1], points[0])
                label = sly.Label(point_ref, reference)
                labels.append(label)

                point_test = sly.Point(points[3], points[2])
                label = sly.Label(point_test, test)
                labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)


    reference = sly.ObjClass("reference point", sly.Point)
    test = sly.ObjClass("test point", sly.Point)

    group_tag_meta = sly.TagMeta(group_tag_name, sly.TagValueType.ANY_STRING)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)

    meta = sly.ProjectMeta(
        obj_classes=[reference, test],
        tag_metas=[group_tag_meta],
    )
    api.project.update_meta(project.id, meta.to_json())
    api.project.images_grouping(id=project.id, enable=True, tag_name=group_tag_name)

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_names = os.listdir(images_path)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for images_names_batch in sly.batched(images_names, batch_size=batch_size):
        img_pathes_batch = [os.path.join(images_path, image_name) for image_name in images_names_batch]

        anns_batch = [create_ann(image_path) for image_path in img_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress.iters_done_report(len(images_names_batch))

    return project
