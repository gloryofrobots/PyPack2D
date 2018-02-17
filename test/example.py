import pypack2d

def json_callback(atlas):
    import json
    images = []
    for image in atlas:
        images.append(dict(
            uv=image.uv,
            path=image.path,
            rotated=image.is_rotated
        ))

    data_path = atlas.get_path_with_extension("json")
    data = dict(
        path=atlas.path,
        images=images
    )
    datafile = open(data_path, "w")
    with datafile as f:
        f.write(json.dumps(data))


pack_settings = dict(
    callback=json_callback,
    # algo=dict(type=pypack2d.PackingAlgorithm.GUILLOTINE, split=pypack2d.GuillotineSplitRule.MAX_AREA),
    algo=pypack2d.PackingAlgorithm.GUILLOTINE,
    heuristic=pypack2d.PlaceHeuristic.BEST_AREA_FIT,
    sort_order=pypack2d.SortOrder.ASC,
    sort_key=pypack2d.SortKey.SIDE_RATIO,
    resize_mode=pypack2d.ResizeMode.NONE,
    packing_mode=pypack2d.PackingMode.LOCAL_SEARCH,

    rotate_mode=pypack2d.RotateMode.NONE,
    max_width=512,
    max_height=512,
    # border=dict(
    #         rect=dict(left=1, top=1, right=1, bottom=1),
    #         type=pypack2d.BorderType.SOLID,
    #         color="#000"
    # ),
    border=dict(
        size=1,
        type=pypack2d.BorderType.PIXELS_FROM_EDGE,
        color="#fff"
    ),
    border_mode=pypack2d.BorderMode.AUTO,

    atlas=dict(
        file_prefix="atlas",
        file_type="png",
        texture_mode="RGBA"
    )
)

stats = pypack2d.pack(["img/test/*.png"], "img/atlas", pack_settings)

print("Count images: %i efficiency : %4.2f " % (stats["count"], stats["efficiency"]))
