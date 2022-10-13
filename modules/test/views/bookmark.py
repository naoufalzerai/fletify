from flet import Text,Image,GridView,border_radius

def bookmark():
    images = GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )


    for i in range(0, 60):
        images.controls.append(
            Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit="none",
                repeat="noRepeat",
                border_radius=border_radius.all(10),
            )
        )
    return images