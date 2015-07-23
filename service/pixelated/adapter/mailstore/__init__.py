#
# Copyright (c) 2015 ThoughtWorks, Inc.
#
# Pixelated is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pixelated is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Pixelated. If not, see <http://www.gnu.org/licenses/>.


class MailStore(object):
    def get_mail(self, mail_id):
        pass

    def get_mails(self, mail_ids):
        pass

    def delete_mail(self, mail_id):
        pass

    def update_mail(self, mail):
        pass

    def add_mail(self, mailbox_name, mail):
        pass

    def get_mailbox_names(self):
        pass

    def get_mailbox_mail_ids(self, mailbox_name):
        pass
