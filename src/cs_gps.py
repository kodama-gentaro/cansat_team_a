from machine import UART
class GPS:
    def __init__(self, uart:UART):
        self.uart = uart

    #緯度(latitude)と経度(longitude)を取得する関数を作って
    def get_coordinate(self):
        latitude = 0
        longitude = 0
        return latitude, longitude
    #目的地までの方向を数値で返す変数を作って(+-180度で)
    def get_heading_to_destination(self):

        return
