import unittest
from robot import Robot

class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.mega_man.say_name(),
            "BEEP BOOP BEEP BOOP. I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)

if __name__ == "__main__":
    unittest.main()


"""
ngày mai làm gì giờ ta
    cày: tiếp tích phân 2 lớp, chắc ôn hết tích phân 2 lớp là mệt lun rùi
    còn tham lam hơn nữa chắc chờ tiếp: xong tích phân 2 lớp rồi sẽ công đánh chương 4

    xác xuất thống kê: chắc làm cho đủ 5 bài ngày hôm này (dứt điểm nợ nần)
    bây h là 23/5 rùi, toang tới nơi rồi?
    khi nào luyện đề 2 môn xác xuất và giải tích 2?
    giải tích còn nhiều thời  gian chứ xác xuất sắp hết time rồi
    mai bớt chơi bời lại lo học

    còn môn vật lý nữa, từ rày đến hôm thi ôn lại 5 dạng điện với 7 dạng từ
    rảnh rảnh ngồi đọc lý thuyết xem có ngộ ra được gì hay không

    còn môn kinh tế nữa
    chắc mình tạm dừng học python với web lại tập trung cho thi kì 2  này
    rồi tiếp tục cũng không muộn, lúc đó mình không bị áp lực các thứ đè lên
    


    từ đây tới lúc thi nè
    24/5 ôn tập
    25/5 ôn tập
    ////trước 25/5 phải ôn xong cho được vật lý/ gt2 và xs
    * 26/6 ôn tập, đọc kinh tế chính trị
    27/5 làm đề vật lý, làm bt kinh tế chính trị
    28/5 làm đề vật lý, làm bt kinh tế chính trị
    29/5 làm đề vật lý, làm bt kinh tế chính trị
    * 30/5 ôn tập xs, đọc kinh tế chính trị
    31/5  ôn tập xs, đọc kinh tế chính trị
    * 1/6 ôn tập xs 
    2/6 làm đề xs, ôn gt2
    3/6 làm đề xs, ôn gt2
    4/6 làm đề xs, ôn gt2
    * 5/6 thi xs
    6/6
    7/6
    * 8/6 thi kĩ thuật lập trình, môn này chưa nghĩ ra chắc là sẽ xem lại rồi mở rộng từ đề của thầy Khánh
"""