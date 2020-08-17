from PIL import Image, ImageDraw, ImageFont
import random

# def main_generate_birthday(path_image, font_size, cor_y, fill):
#     for count in range(250):
#         img = Image.open(path_image)
#         img_name = img.filename.split("/")[-1].split(".")[0]
#         img_w, img_h = img.size
#         fnt = ImageFont.truetype('/home/minhpv/Desktop/tools/Fonts/palab.ttf', font_size)
#         random_move_y = random.randint(-3, 3)
#         random_day = random.randint(1, 31)
#         if random_day < 10:
#             random_day = "0" + str(random_day)
#         random_year = random.randint(1800, 2100)
#         ran_month = random.randint(1, 12)
#         if ran_month < 10:
#             ran_month = "0" + str(ran_month)
#         text = "{}-{}-{}".format(random_day, ran_month, random_year)
#         (width, baseline), (offset_x, offset_y) = fnt.font.getsize(text)
#         padding_x = random.randint(10, img_w - width - 10)
#         d = ImageDraw.Draw(img)
#         d.text((padding_x, cor_y + random_move_y), text, font=fnt, fill=fill)
#         # img = img.crop((offset_x, offset_y, offset_x + width, offset_y + baseline))
#         img.save('/home/minhpv/Desktop/tools/data_gens/card_birthday/%s.jpg' %(img_name + "-" + str(count)))
#
# # path_image = r'/home/minhpv/Desktop/tools/datas/card_birthday/1.jpg'
# # font_size = 20
# # cor_y = 12
# # fill = (30, 30, 30)
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/1.jpg', 20, 12, (30, 30, 30))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/2.jpg', 24, 14, (30, 30, 30))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/3.jpg', 50, 36, (30, 30, 30))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/4.jpg', 24, 14, (50, 50, 50))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/5.jpg', 34, 24, (30, 30, 30))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/7.jpg', 36, 18, (50, 50, 50))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/8.jpg', 50, 34, (30, 30, 30))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/9.jpg', 140, 120, (100, 100, 100))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/10.jpg', 14, 8, (30, 30, 30))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/11.jpg', 52, 34, (50, 50, 50))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/12.jpg', 56, 46, (30, 30, 30))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/13.jpg', 84, 52, (30, 30, 30))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/14.jpg', 80, 44, (30, 30, 30))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/15.jpg', 80, 48, (90, 90, 90))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/16.jpg', 110, 74, (60, 60, 60))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/17.jpg', 100, 70, (30, 30, 30))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/18.jpg', 70, 50, (80, 80, 80))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/19.jpg', 38, 12, (50, 50, 50))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/20.jpg', 70, 34, (30, 30, 30))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/21.jpg', 74, 64, (30, 30, 30))
# main_generate_birthday(r'/home/minhpv/Desktop/tools/datas/card_birthday/22.jpg', 30, 12, (60, 60, 60))


#############################################################################################################################
##### card name

# def main_generate_name(path_img, font_size, text_gen1, cor_y, cor_y_sub, fill):
#     # text = text_gen[0]
#     # text_sub = text_gen[1]
#     for i in range(250):
#         text_gen = get_name()
#         text = text_gen[0]
#         text_sub = text_gen[1]
#         random_move_y = random.randint(-3, 3)
#         img = Image.open(path_img)
#         img_w, img_h = img.size
#         img_name = img.filename.split("/")[-1].split(".")[0]
#         fnt = ImageFont.truetype('/home/minhpv/Desktop/tools/Fonts/palab.ttf', font_size)
#         (width, baseline), (offset_x, offset_y) = fnt.font.getsize(text)
#         (width_sub, baseline_sub), (offset_x_sub, offset_y_sub) = fnt.font.getsize(text_sub)
#         if img_w - width - 10 > 10 and img_w - width_sub - 10 > 10:
#             padding_x = random.randint(10, img_w - width - 10)
#             padding_x_sub = random.randint(10, img_w - width_sub - 10)
#             d = ImageDraw.Draw(img)
#             d.text((padding_x, cor_y + random_move_y), text, font=fnt, fill=fill)
#             # img.save('/home/minhpv/Desktop/tools/data_gens/card_name/%s.jpg' % (img_name + "-" + str(i)))
#             d.text((padding_x_sub, cor_y_sub + random_move_y), text_sub, font=fnt, fill=fill)
#             img.save('/home/minhpv/Desktop/tools/data_gens/card_name/%s.jpg' % (img_name + "-" + str(i)))
#         else:
#             print(img_name)
#
# ho = "Dương,Lỗ,Lục,Ngũ,Phan,Vi,Vủ,Bá,Bạch,Báo,Bố,Châu,Chế,Chiêm,Cửu,Dụng,Dương,Ðàng,Ðạo,Ðạt,Ðổng,Fatimah,Hàm,Hán,Hứa,Kiều,KimLa,Lâm,Lộ,Lưu,Ma,Mahomach,Mang,Mân,Miêu,Nại,Não,Nguyễn,Ông,Phú,Qua,QuảngÐại,Sa,Tài,Từ,Thành,Thập,Thị,Thiên,Thiết,Thổ,Thuận,Trà,Trương,Trượng,Văn," \
#      "A,Ai,An,Áo,Ân,Âu,Bá,Bà,Bạc,Bạch,Bàn,Bàng,Bành,Bảo,Bạt,Bằng,Bê,Bế,Bi,Bì,Bia,Biên,Biện,Bình,Bố,Bồ,Bổ,Bôi,Bông,Bu,Bùi,Ca,Cả,Cai,Cái,Cam,Cảm,Can,Càng,Cánh,Cảnh,Cao,Cáo,Cáp,Cát,Căn,Cắt,Cầm,Cần,Cấn,Chan,Châm,Chân,Châu,Chế,Chi,Chim,Chiêm,Chiều,Chu,Chúc,Chung,Chuyên,Chử,Chức,Chương,Cô,Cố,Cổ,Cốc,Công,Công,Côn,Tôn,Cống,Cù,Cung,Cự,Cửu,Dã,Danh," \
#      "Dân,Dì,Dị,Diệc,Diệp,Diêu,Diệu,Doãn,Dụ,Dung,Duy,Dư,Dương,Ða,Ðác,Ðái,Ðàm,Ðan,Ðào,Ðạo,Ðắc,Ðằng,Ðặng,Ðấu,Ðẩu,Ðậu,Ðèo,Ðiêm,Ðiền,Ðiệp,Ðiêu,Ðiều,Ðiểu,Ðiệu,Ðịch,Ðinh,Ðình,Ðịnh,Ðoái,Ðoàn,Ðồ,Ðỗ,Ðối,Ðôn,Ðông,Ðồng,Ðống,Ðổng,Đức,Ðường,Gan,Giao,Giản,Giang,Giáng,Giao,Giáp,Giệp,Gioãn,Giốc,Gương,Hà,Há,Hạ,Hai,Hàm,Hàn,Hán,Hang,Hàng,Hạnh,Hào,Hảo,Hạp,Hâm,Hầu,Hê,Hi,Hinh,Hình," \
#      "Hò,Hoa,Hoài,Hoan,Hoàng,Huỳnh,Hoắc,Hồ,Hội,Hồng,Hung,Hùng,Hui,Huy,Hứa,Hương,Hướng,Kan,Kem,Kha,Khả,Khâm,Khâu,Kheo,Khiên,Khiếu,Khôi,Khổng,Khu,Khuất,Khúc,Khương,Khưu,Kiên,Kiện,Kiều,Kiệu,Kim,Kỷ,La,Lã,Lại,Lang,Lanh,Lãnh,Lão,Lăng,Lâm,Lầu,Lê," \
#      "Lều,Lịch,Liêm,Liên,Liêng,Liêu,Liễu,Linh,Lĩnh,Liu,Lò,Lô,Lỗ,Lộ,Lộc,Lôi,Lợi,Lù,Lục,Luyện,Lữ,Lương,Lưu,Lý,Ma,Mã,Mạc,Mạch,Mai,Man,Mang,Mạnh,Mao,Mẫn,Mật,Mậu,Mẫu,Mị,MiênMinh,Mục,Mùi,Nan,Nga,Ngạc,Ngân,Nghê,Nghi,Nghĩa,Nghiêm,Nghiên,Ngọ,Ngọc,Ngô,Ngũ," \
#      "Ngụy,Nguyễn,Ngư,Ngưu,Nhã,Nham,Nhan,Nhạn,Nhâm,Nhân,Nhất,Nhiếp,Nhung,Niên,Ninh,Nông,Nung,Nùng,On,Ong,Ô,Ôn,Ông,Phạm,Phan,Phàn,Phẩm,Phí,Phó,Phòng,Phô,Phù,Phú,Phúc,Phùng,Phương,Quách,Quan,Quản,Quang,Quảng,Quấc,Quân,Quất,Quyên," \
#      "Quyến,Quyền,Quỳnh,Roãn,Sa,Sái,Sam,Sâm,Sầm,Sẩm,Sĩ,Sở,Sơn,Sử,Sưu,Tạ,Tán,Tang,Tào,Tạo,Tảo,Tắc,Tăng,Tân,Tần,Tất,Teo,Tha,Thạc,Thạch,Thái,Thang," \
#      "Thanh,Thành,Thảo,Thẩm,Thân,Thê,Thể,Thềm,Thi,Thiên,Thiện,Thiết,Thiệt,Thiều,Thiệu,Thịnh,Thông,Thôi,Thủ,Thục,Thượng,Ti,Tích,Tiên,Tiến,Tiệt,Tiêu,Toàn,Tô,Tôn," \
#      "Tống,Tuyên,Trà,Trác,Trang,Trầm,Trần,Tri,Trí,Triển,Triệu,Trình,Trịnh,Trong,Tru,Trung,Trừ,Trực,Trưng,Trương,Trượng,Tuân,Tuấn,Tùng,Tư,Từ,Tường,Tướng,Tưởng,Tượng,U,Ủ,Uất,Ung,Uông,Uyển,Ưng,Ứng,Ửng,Vạn,Văn,Vân,Vận,Vầu,Vệ,Vi,Viêm,Viên,Viết,Vinh,Vĩnh,Vịnh,Vu,Vũ,Vòng,Vỏng,Vô,Vù,Vương,Vưu,Vỹ,Xa,Xuân,Yết"
# HO = ho.split(",")
# HO = [i for i in HO if len(i) > 1]
#
# def get_name():
#     lengt_name = random.randint(2, 10)
#     if lengt_name == 2:
#         name = random.choice(HO) + " " + random.choice(HO)
#         name_sub = ""
#     else:
#         name = random.choice(HO) + " " + random.choice(HO) + " " + random.choice(HO)
#         lengt_name_sub = random.randint(0, 2)
#         if lengt_name_sub == 0:
#             name_sub = ""
#         elif lengt_name_sub == 1:
#             name_sub = random.choice(HO)
#         else:
#             name_sub = random.choice(HO) + " " + random.choice(HO)
#     return [name.upper(), name_sub.upper()]
#
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/1.jpg', 24, get_name(), 12, 44, (30 , 30, 30))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/2.jpg', 50, get_name(), 40, 130, (50 , 50, 50))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/3.jpg', 60, get_name(), 64, 176, (30 , 30, 30))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/4.jpg', 100, get_name(), 110, 270, (70 , 70, 70))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/5.jpg', 24, get_name(), 12, 44, (30 , 30, 30))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/6.jpg', 62, get_name(), 64, 190, (80 , 80, 80))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/7.jpg', 64, get_name(), 66, 186, (50 , 50, 50))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/8.jpg', 120, get_name(), 90, 260, (30 , 30, 30))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/9.jpg', 70, get_name(), 50, 170, (20 , 20, 20))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/10.jpg', 70, get_name(), 70, 200, (60 , 60, 60))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/11.jpg', 50, get_name(), 22, 74, (56, 56, 56))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/12.jpg', 40, get_name(), 20, 72, (30, 30, 30))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/13.jpg', 60, get_name(), 60, 160, (30, 30, 30))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/14.jpg', 24, get_name(), 20, 60, (30, 30, 30))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/15.jpg', 24, get_name(), 20, 62, (70, 70, 70))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/16.jpg', 50, get_name(), 40, 120, (30, 30, 30))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/17.jpg', 120, get_name(), 120, 360, (80, 80, 80))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/18.jpg', 24, get_name(), 16, 50, (30, 30, 30))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/19.jpg', 72, get_name(), 80, 200, (30, 30, 30))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/20.jpg', 60, get_name(), 36, 120, (50, 50, 50))
# main_generate_name(r'/home/minhpv/Desktop/tools/datas/card_name/21.jpg', 100, get_name(), 130, 350, (50, 50, 50))

###########################################################################################################################
######### INFO

# street = ["Thị xã", "Thôn", "xã", "TX.", "X.", "P.", "Xã", "Thị trấn"]
# city = ["Huyện", "huyện", "Tỉnh", "tỉnh", "TX.", "Thị trấn", "TP.", "P.", "X."]
# name_street = ["Bạch Mai",
#                "Bà Triệu",
#                "Cầu Giấy",
#                "Hồ Tùng Mậu",
#                "Tam Trinh",
#                "Giải Phóng",
#                "Đê La Thành",
#                "Phố Huế",
#                "Hoàng Cầu",
#                "Nguyễn Chí Thanh",
#                "Chùa Láng",
#                "Trung Kính",
#                "Đinh Lễ",
#                "Phố Vọng",
#                "Văn Cao",
#                "Phạm Ngọc Thạch",
#                "Chùa Bộc",
#                "Thái Thịnh",
#                "Lò Đúc",
#                "Trương Định",
#                "Đại La",
#                "Định Công",
#                "Thụy Khuê",
#                "Nguyễn Xiển",
#                "Phạm Hùng",
#                "Phố Huế",
#                "Cầu Đất",
#                "Kim Ngưu",
#                "Nguyên Hồng",
#                "Quán Thánh",
#                "Nguyễn Du",
#                "Lý Thường Kiệt",
#                "Ngọc Khánh",
#                "Đường Láng"
#                "Lê Đức Thọ"
#                "Khương Trung"
#                "Khuất Duy Tiến"
#                "Dương Quảng Hàm"
#                "Ngõ Huyện"
#                "Nguyễn Xiển"]
# huyen = ["An Khê", "An Nhơn", "Ayun Pa", "Ba Đồn", "Bến Cát", "Bỉm Sơn", "Bình Long", "Bình Minh", "Buôn Hồ", "Cai Lậy",
#          "Cửa Lò", "Duy Tiên", "Duyên Hải", "Điện Bàn"
#     , "Đông Hòa", "Đông Triều", "Đức Phổ", "Giá Rai", "Gò Công", "Hoà Thành", "Hoài Nhơn", "Hoàng Mai", "Hồng Lĩnh",
#          "Hồng Ngự", "Hương Thủy", "Hương Trà", "Kiến Tường"
#     , "Kinh Môn", "Kỳ Anh", "La Gi", "Long Mỹ", "Mường Lay", "Mỹ Hào", "Ngã Năm", "Nghi Sơn", "Nghĩa Lộ", "Ninh Hòa",
#          "Phổ Yên", "Phú Mỹ", "Phú Thọ", "Phước Long"
#     , "Quảng Trị", "Quảng Yên", "Sa Pa", "Sông Cầu", "Sơn Tây", "Tân Châu", "Tân Uyên", "Thái Hòa", "Trảng Bàng",
#          "Từ Sơn", "Vĩnh Châu"]
# tinh = ["Bà Rịa", "Bạc Liêu", "Bảo Lộc", "Bắc Giang", "Bắc Kạn", "Bắc Ninh", "Bến Tre", "Biên Hòa", "Buôn Ma Thuột",
#         "Cà Mau", "Cam Ranh", "Cao Bằng", "Cao Lãnh", "Cẩm Phả", "Châu Đốc", "Chí Linh",
#         "Dĩ An", "Đà Lạt", "Điện Biên Phủ", "Đông Hà", "Đồng Hới", "Đồng Xoài", "Gia Nghĩa", "Hà Giang", "Hạ Long",
#         "Hà Tiên", "Hà Tĩnh", "Hải Dương", "Hòa Bình", "Hội An", "Huế", "Hưng Yên", "Kon Tum", "Lai Châu"
#     , "Lạng Sơn", "Lào Cai", "Long Khánh", "Long Xuyên", "Móng Cái", "Mỹ Tho", "Nam Định", "Ngã Bảy", "Nha Trang",
#         "Ninh Bình", "Phan Thiết", "Phủ Lý", "Phúc Yên", "Pleiku",
#         "Quảng Ngãi", "Quy Nhơn", "Rạch Giá", "Sa Đéc", "Sầm Sơn", "Sóc Trăng", "Sơn La", "Sông Công", "Tam Điệp",
#         "Tam Kỳ", "Tân An", "Tây Ninh", "Thái Bình", "Thái Nguyên", "Thanh Hóa", "Thủ Dầu Một",
#         "Thuận An", "Trà Vinh", "Tuy Hòa", "Tuyên Quang", "Uông Bí", "Vị Thanh", "Việt Trì", "Vinh", "Vĩnh Long",
#         "Vĩnh Yên", "Vũng Tàu", "Yên Bái"]
#
#
# def main_generate_info(path_img, font_size, text11, text21, text31, text41, padding_1, cor_1, padding_2, cor_2,
#                        padding_3, cor_3, padding_4, cor_4, fill):
#     done = 0
#     sl = 250
#     for i in range(sl):
#         text1 = random.choice(street) + " " + random.choice(name_street)
#         text2 = random.choice(street) + " " + random.choice(huyen) + ", " + random.choice(city) + " " + random.choice(
#             tinh)
#         text3 = random.choice(street) + " " + random.choice(name_street)
#         text4 = random.choice(street) + " " + random.choice(huyen) + ", " + random.choice(city) + " " + random.choice(
#             tinh)
#         random_move_y = random.randint(-3, 3)
#         img = Image.open(path_img)
#         img_w, img_h = img.size
#         img_name = img.filename.split("/")[-1].split(".")[0]
#         fnt = ImageFont.truetype('/home/minhpv/Desktop/tools/Fonts/palab.ttf', font_size)
#         (width1, baseline1), (offset_x1, offset_y1) = fnt.font.getsize(text1)
#         (width2, baseline2), (offset_x2, offset_y2) = fnt.font.getsize(text2)
#         (width3, baseline3), (offset_x3, offset_y3) = fnt.font.getsize(text3)
#         (width4, baseline4), (offset_x4, offset_y4) = fnt.font.getsize(text4)
#
#         # if img_w - width - 10 > 0 and img_w - width_sub - 10 > 0:
#         if img_w - width1 - 5 > 0 and img_w - width2 - 5 > 0 and img_w - width3 - 5 > 0 and img_w - width4 - 5 > 0:
#             padding_x1 = random.randint(5, img_w - width1 - 5)
#             padding_x2 = random.randint(5, img_w - width2 - 5)
#             padding_x3 = random.randint(5, img_w - width3 - 5)
#             padding_x4 = random.randint(5, img_w - width4 - 5)
#             d = ImageDraw.Draw(img)
#             # d.text((padding_x, cor_y + random_move_y), text, font=fnt, fill=fill)
#             d.text((padding_x1, cor_1 + random_move_y), text1, font=fnt, fill=fill)
#             d.text((padding_x2, cor_2 + random_move_y), text2, font=fnt, fill=fill)
#             d.text((padding_x3, cor_3 + random_move_y), text3, font=fnt, fill=fill)
#             d.text((padding_x4, cor_4 + random_move_y), text4, font=fnt, fill=fill)
#             # img.save('/home/minhpv/Desktop/tools/data_gens/card_name/%s.jpg' % (img_name + "-" + str(i)))
#             img.save('/home/minhpv/Desktop/tools/data_gens/card_info/%s.jpg' % (img_name + "-" + str(i)))
#             done += 1
#         else:
#             print(img_name)
#     print("Thiếu " + str(sl-done))
#
#
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/1.jpg', 20, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa",
#                    "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 120, 10, 40, 45, 180, 76, 50, 110, (50, 50, 50))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/2.jpg', 22, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 130, 14, 40, 50, 210, 88, 50, 123, (70,70,70))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/3.jpg', 23, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 135, 15, 40, 52, 210, 88, 50, 124, (70,70,70))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/4.jpg', 50, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 300, 24, 40, 110, 460, 190, 50, 270, (50,50,50))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/5.jpg', 150, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 920, 72, 40, 330, 1400, 580, 400, 800, (100,100,100))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/6.jpg', 40, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 200, 16, 40, 70, 300, 124, 50, 180, (35,35,35))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/7.jpg', 50, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 310, 30, 40, 110, 460, 200, 50, 275, (60,60,60))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/8.jpg', 26, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 140, 12, 30, 52, 210, 90, 60, 124, (50,50,50))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/9.jpg', 14, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 76, 6, 40, 26, 114, 46, 30, 66, (60,60,60))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/10.jpg', 150, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 830, 50, 40, 300, 1300, 540, 50, 760, (70,70,70))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/11.jpg', 80, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa",430, 40, 40, 160, 660, 270, 50, 376, (30,30,30))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/12.jpg', 80, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 450, 38, 40, 164, 680, 272, 50, 390, (50,50,50))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/13.jpg', 80, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 440, 40, 40, 154, 650, 276, 50, 380, (50,50,50))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/14.jpg', 120, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 650, 50, 40, 230, 1000, 408, 50, 574, (40,40,40))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/15.jpg', 38, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 200, 14, 40, 74, 310, 126, 50, 176, (40,40,40))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/16.jpg', 74, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 450, 40, 40, 170, 680, 290, 50, 410, (50,50,50))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/17.jpg', 70, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 450, 50, 40, 180, 680, 300, 50, 420, (50,50,50))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/18.jpg', 34, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 200, 18, 40, 70, 300, 120, 50, 172, (30,30,30))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/19.jpg', 54, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 340, 24, 40, 122, 520, 210, 50, 300, (30,30,30))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/20.jpg', 110, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 660, 80, 40, 260, 1000, 440, 50, 610, (50,60,60))
# main_generate_info(r'/home/minhpv/Desktop/tools/datas/card_info/21.jpg', 16, "Quang Trung", "Thị xã Bỉm Sơn, Thanh Hóa", "P. Phú Sơn", "Thị xã Bỉm Sơn, Thanh Hóa", 94, 8, 40, 34, 140, 58, 50, 78, (30,30,30))

##########################################################################################
# words = ["Thị", "xã", "Thôn", "xã", "TX.", "X.", "P.", "Xã", "Thị trấn", "Huyện", "huyện", "Tỉnh", "tỉnh", "TX.", "Thị",
#          "trấn", "TP.", "P.", "X.",
#          "An Khê", "An", "Nhơn", "Ayun", "Pa", "Ba", "Đồn", "Bến", "Cát", "Bỉm", "Sơn", "Bình", "Long", "Bình", "Minh",
#          "Buôn", "Hồ", "Cai", "Lậy",
#          "Cửa", "Lò", "Duy", "Tiên", "Duyên", "Hải", "Điện", "Bàn"
#     , "Đông", "Hòa", "Đông", "Triều", "Đức", "Phổ", "Giá", "Rai", "Gò", "Công", "Hoà", "Thành", "Hoài", "Nhơn", "Hoàng",
#          "Mai", "Hồng", "Lĩnh",
#          "Hồng", "Ngự", "Hương", "Thủy", "Hương", "Trà", "Kiến", "Tường"
#     , "Kinh", "Môn", "Kỳ", "Anh", "La", "Gi", "Long", "Mỹ", "Mường", "Lay", "Mỹ", "Hào", "Ngã", "Năm", "Nghi", "Sơn",
#          "Nghĩa", "Lộ", "Ninh", "Hòa",
#          "Phổ", "Yên", "Phú", "Mỹ", "Phú", "Thọ", "Phước", "Long"
#     , "Quảng", "Trị", "Quảng", "Yên", "Sa", "Pa", "Sông", "Cầu", "Sơn", "Tây", "Tân", "Châu", "Tân", "Uyên", "Thái",
#          "Hòa", "Trảng", "Bàng",
#          "Từ", "Sơn", "Vĩnh", "Châu",
#          "Bà", "Rịa", "Bạc", "Liêu", "Bảo", "Lộc", "Bắc", "Giang", "Bắc", "Kạn", "Bắc", "Ninh", "Bến", "Tre", "Biên",
#          "Hòa", "Buôn", "Ma", "Thuột",
#          "Cà", "Mau", "Cam", "Ranh", "Cao", "Bằng", "Cao", "Lãnh", "Cẩm", "Phả", "Châu", "Đốc", "Chí", "Linh",
#          "Dĩ", "An", "Đà", "Lạt", "Điện", "Biên", "Phủ", "Đông", "Hà", "Đồng", "Hới", "Đồng", "Xoài", "Gia", "Nghĩa",
#          "Hà", "Giang",
#          "Hạ", "Long",
#          "Hà", "Tiên", "Hà", "Tĩnh", "Hải", "Dương", "Hòa", "Bình", "Hội", "An", "Huế", "Hưng", "Yên", "Kon", "Tum",
#          "Lai", "Châu"
#     , "Lạng", "Sơn", "Lào", "Cai", "Long", "Khánh", "Long", "Xuyên", "Móng", "Cái", "Mỹ", "Tho", "Nam", "Định", "Ngã",
#          "Bảy", "Nha", "Trang",
#          "Ninh", "Bình", "Phan", "Thiết", "Phủ", "Lý", "Phúc", "Yên", "Pleiku",
#          "Quảng", "Ngãi", "Quy", "Nhơn", "Rạch", "Giá", "Sa", "Đéc", "Sầm", "Sơn", "Sóc", "Trăng", "Sơn", "La", "Sông",
#          "Công", "Tam", "Điệp",
#          "Tam", "Kỳ", "Tân", "An", "Tây", "Ninh", "Thái", "Bình", "Thái", "Nguyên", "Thanh", "Hóa", "Thủ", "Dầu", "Một",
#          "Thuận", "An", "Trà", "Vinh", "Tuy", "Hòa", "Tuyên", "Quang", "Uông", "Bí", "Vị", "Thanh", "Việt", "Trì",
#          "Vinh", "Vĩnh", "Long",
#          "Vĩnh", "Yên", "Vũng", "Tàu", "Yên", "Bái"
#          ]
#
#
# def info(path_img, size, cor_y, fill):
#     for i in range(2):
#         img = Image.open(path_img)
#         img_name = img.filename.split("/")[-1].split(".")[0]
#         img_w, img_h = img.size
#         fnt = ImageFont.truetype('/home/minhpv/Desktop/tools/Fonts/palab.ttf', size)
#         random_move_y = random.randint(-4, 4)
#         text = random.choice(words)
#         (width, baseline), (offset_x, offset_y) = fnt.font.getsize(text)
#         if img_w - width - 5 > 5:
#             padding_x = random.randint(5, img_w - width - 5)
#             d = ImageDraw.Draw(img)
#             d.text((padding_x, cor_y + random_move_y), text, font=fnt, fill=fill)
#             img.save('/home/minhpv/Desktop/tools/data_gens/card_info/%s.jpg' %(img_name + "-c" + str(i)))
#         else:
#             print(img_name)


# info(r"/home/minhpv/Desktop/tools/datas/card_info/1.jpg", 60, 24, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/2.jpg", 70, 25, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/3.jpg", 60, 25, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/4.jpg", 55, 25, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/5.jpg", 70, 55, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/6.jpg", 60, 22, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/7.jpg", 40, 10, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/8.jpg", 70, 40, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/9.jpg", 70, 40, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/10.jpg", 80, 55, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/11.jpg", 60, 24, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/12.jpg", 60, 20, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/13.jpg", 50, 30, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/14.jpg", 60, 24, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/15.jpg", 60, 24, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/16.jpg", 22, 15, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/17.jpg", 60, 24, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/18.jpg", 22, 18, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/19.jpg", 60, 40, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/20.jpg", 68, 40, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/21.jpg", 64, 44, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/22.jpg", 62, 50, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/23.jpg", 60, 35, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/24.jpg", 70, 36, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/25.jpg", 90, 80, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/26.jpg", 60, 50, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/27.jpg", 90, 70, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/28.jpg", 25, 10, (40,40,40))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/29.jpg", 110, 60, (40,40,40))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/30.jpg", 90, 70, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/31.jpg", 100, 70, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/32.jpg", 120, 80, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/33.jpg", 120, 80, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/34.jpg", 120, 80, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/35.jpg", 60, 31, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/36.jpg", 120, 60, (50,50,50))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/37.jpg", 90, 30, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/38.jpg", 90, 30, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/39.jpg", 25, 10, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/40.jpg", 20, 10, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/41.jpg", 20, 10, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/42.jpg", 65, 50, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/43.jpg", 25, 15, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/44.jpg", 20, 10, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/45.jpg", 30, 15, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/46.jpg", 50, 50, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/47.jpg", 60, 50, (50,50,50))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/48.jpg", 70, 40, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/49.jpg", 60, 40, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/50.jpg", 60, 35, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/51.jpg", 50, 45, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/52.jpg", 50, 50, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/53.jpg", 70, 30, (50,50,50))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/54.jpg", 70, 40, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/55.jpg", 80, 70, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/56.jpg", 90, 60, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/57.jpg", 110, 85, (40,40,40))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/58.jpg", 100, 60, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/59.jpg", 40, 30, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/60.jpg", 110, 80, (80,80,80))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/61.jpg", 50, 25, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/62.jpg", 70, 36, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/63.jpg", 34, 15, (60,60,60))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/64.jpg", 70, 60, (80,80,80))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/65.jpg", 24, 12, (50,50,50))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/66.jpg", 80, 60, (80,80,80))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/67.jpg", 40, 25, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/68.jpg", 30, 15, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/69.jpg", 70, 60, (50,50,50))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/70.jpg", 80, 50, (50,50,50))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/71.jpg", 80, 60, (50,50,50))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/72.jpg", 70, 50, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/73.jpg", 85, 62, (60,60,60))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/74.jpg", 80, 60, (30,30,30))
# info(r"/home/minhpv/Desktop/tools/datas/card_info/75.jpg", 70, 50, (50,50,50))

##########################################################################################

def generate_number(path_img, size, cor_y, fill):
    for i in range(250):
        img = Image.open(path_img)
        img_name = img.filename.split("/")[-1].split(".")[0]
        img_w, img_h = img.size
        fnt = ImageFont.truetype('/home/minhpv/Desktop/tools/Fonts/Berthold_Akzidenz_Grotesk_Medium_Extended.otf', size)
        random_move_y = random.randint(-4, 4)
        text = random.randint(100000000, 999999999)
        (width, baseline), (offset_x, offset_y) = fnt.font.getsize(str(text))
        if img_w - width - 5 > 5:
            padding_x = random.randint(5, img_w - width - 5)
            d = ImageDraw.Draw(img)
            d.text((padding_x, cor_y + random_move_y), str(text), font=fnt, fill=fill)
            img.save('/home/minhpv/Desktop/tools/data_gens/id/%s.jpg' %(img_name + "-" + str(i)))
        else:
            print(img_name)

generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/1.jpg', 28, 9, (30,30,30))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/2.jpg', 30, 9, (30,30,30))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/3.jpg', 140, 30, (30,30,30))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/4.jpg', 190, 20, (40,40,40))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/5.jpg', 100, 20, (30,30,30))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/6.jpg', 110, 9, (50,50,50))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/7.jpg', 110, 9, (50,50,50))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/8.jpg', 95, 20, (50,50,50))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/9.jpg', 40, 9, (65,65,65))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/10.jpg', 26, 9, (60,60,60))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/11.jpg', 30, 9, (50,50,50))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/12.jpg', 85, 9, (30,30,30))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/13.jpg', 130, 30, (40,40,40))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/14.jpg', 95, 20, (30,30,30))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/15.jpg', 65, 9, (40,40,40))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/16.jpg', 42, 9, (40,40,40))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/17.jpg', 70, 20, (30,30,30))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/18.jpg', 65, 20, (50,50,50))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/19.jpg', 28, 9, (30,30,30))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/20.jpg', 85, 20, (50,50,50))
generate_number(r'/home/minhpv/Desktop/tools/datas/card_number/21.jpg', 38, 12, (20,20,20))

