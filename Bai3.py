from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

#
# This is the Python code that makes this feedback form work.
# It's a Python class, with a method that runs when the user
# clicks the SUBMIT button.
#
# When the button is clicked, we send the contents of the
# text boxes to our Server Module. The Server Module records
# the feedback in the database, and sends an email to the
# app's owner (that's you!).
#
# To find the Server Module, look under "Server Code" on the
# left.
#

class HomeForm(HomeFormTemplate):
  def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Khởi tạo danh sách arr
        self.arr = []

  def insertion_sort(self):
      for i in range(1, len(self.arr)):
          key = self.arr[i]
          j = i - 1
          while j >= 0 and self.arr[j] > key:
              self.arr[j + 1] = self.arr[j]
              j -= 1
          self.arr[j + 1] = key

  def btn_Sort_click(self, **event_args):
      input_string = self.txt_NhapSo.text
      string_list = input_string.split()
      # Chuyển đổi các phần tử của danh sách từ chuỗi sang số nguyên
      self.arr = [int(item) for item in string_list]
      self.insertion_sort()
      self.text_box_1.text = ' '.join(map(str, self.arr))
  # Hiển thị kết quả sắp xếp

  def txt_NhapSo_change(self, **event_args):
      # Xóa sự kiện "change" trước khi gán lại để tránh việc gọi đệ quy vô hạn
      self.txt_NhapSo.set_event_handler("change", self.txt_NhapSo_change)

  def btn_Restart_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_1.text = ""
    self.txt_NhapSo.text = ""
    self.arr = []
    pass
