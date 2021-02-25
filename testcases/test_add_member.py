import pytest
import yaml

from page.app import App


def get_add_data(add):
    with open("../data/data.yml", encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        # print(data["add"])
        return data[add]


class TestAddMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phone,mailbox", get_add_data("add"))
    def test_add_member(self, name, gender, phone, mailbox):
        # name = "Zoro"
        # gender = "男"
        # phone = "10000000003"
        # mailbox = "Zoro@163.com"
        toast = self.main.click_address_book().click_add_member().click_add_manually() \
            .edit_name(name).edit_gender(gender).edit_phone(phone).edit_mailbox(mailbox).click_save().get_toast()
        assert toast == "添加成功"
