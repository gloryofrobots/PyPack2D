from pypack2d.field2d import Field2D
from PIL import Image, ImageDraw


class BorderDraw(object):
    def draw(self, atlas_image, border):
        return self._on_draw(atlas_image, border)

    def _on_draw(self, atlas_image, border):
        raise NotImplementedError()

    @staticmethod
    def border_image(w, h):
        return Image.new("RGBA", (w, h), (255, 0, 255))


class BorderDrawRectangle(BorderDraw):
    def _on_draw(self, atlas_image, border):
        new_width = atlas_image.width + border.width
        new_height = atlas_image.height + border.height

        new_image = self.border_image(new_width, new_height)
        img = atlas_image.get_pil_image()
        new_image.paste(img, (border.left, border.top))
        right_edge = new_width - 1
        bottom_edge = new_height - 1

        draw = ImageDraw.Draw(new_image)
        if border.left is not 0:
            line = [(0, 0), (0, bottom_edge)]
            draw.line(line, fill=border.color, width=border.left)

        if border.top is not 0:
            line = [(0, 0), (right_edge, 0)]
            draw.line(line, fill=border.color, width=border.top)

        if border.right is not 0:
            line = [(right_edge, 0), (right_edge, bottom_edge)]
            draw.line(line, fill=border.color, width=border.right)

        if border.bottom is not 0:
            line = [(0, bottom_edge), (right_edge, bottom_edge)]
            draw.line(line, fill=border.color, width=border.bottom)

        return new_image


class BorderDrawEdge(BorderDraw):
    def _on_draw(self, atlas_image, border):
        new_width = atlas_image.width + border.width
        new_height = atlas_image.height + border.height

        new_image = self.border_image(new_width, new_height)
        img = atlas_image.get_pil_image()
        new_image.paste(img, (border.left, border.top))
        data = list(new_image.getdata())
        field = Field2D(data, new_width, new_height)
        # print(self.height,newHeight)
        # Copying data to box around
        if border.top is not 0:
            # print("copy top")
            # top Lines
            source_line = border.top
            line_numbers = range(0, source_line)
            self.copy_lines(field, source_line, line_numbers)

        if border.bottom is not 0:
            # print("copy bottom")
            # bottom lines+
            source_line = atlas_image.height + border.top - 1
            line_numbers = range(source_line + 1, new_height)

            self.copy_lines(field, source_line, line_numbers)

        if border.left is not 0:
            # print("copy left")
            # left columns
            source_column = border.left
            column_numbers = range(0, source_column)
            self.copy_columns(field, source_column, column_numbers)

        if border.right is not 0:
            # print("copy right")
            # right columns
            source_column = atlas_image.width + border.left - 1
            column_numbers = range(source_column + 1, new_width)

            self.copy_columns(field, source_column, column_numbers)

        new_image.putdata(data)
        return new_image

    @staticmethod
    def copy_lines(field, source_line_number, line_numbers):
        for line_number in line_numbers:
            # print("copyLine",source_line_number,line_number)
            field.copy_line(field, source_line_number, line_number)

    @staticmethod
    def copy_columns(field, source_column_number, column_numbers):
        for column_number in column_numbers:
            # print("copyColumn",source_column_number,column_number)
            field.copy_column(field, source_column_number, column_number)
