#!/usr/bin/env python

from .base import Base


class ManageAcl(Base):
    """Say hello, world!"""

    def run(self):
        setacl, readacl, writeacl = (False, False, False)
        alias = self.options['<alias>']
        username = self.options.get('<user>', None)
        if self.options.get('--noread'):
            setacl = True
            readacl = False
        if self.options.get('--read'):
            setacl = True
            readacl = True
        if self.options.get('--nowrite'):
            setacl = True
            writeacl = False
        if self.options.get('--write'):
            setacl = True
            writeacl = True
        if setacl:
            acl = {'username': username,
                   'permission': {'read': readacl,
                                  'write': writeacl}}
            self.store.put_alias_acl(alias, acl)

        self._listacl(alias, username)

    def _listacl(self, alias, username):
        acl_list = self.store.get_alias_acls(alias, username)
        # Agave metadata, which underlies the alias library, will return
        # an empty response if a user does not have any permission assigned.
        # In an interactive setting, this is confusing, so we mock up
        # an ACL and return it in the listing.
        if len(acl_list) < 1:
            fake_acl = {'username': username,
                        'permission': {'read': False,
                                       'write': False}}
            acl_list.append(fake_acl)
        for acl in acl_list:
            print("{} - read: {} write: {}".format(
                acl.get('username'),
                acl.get('permission').get('read'),
                acl.get('permission').get('write')))
        # print('You supplied the following options:', dumps(
        #     self.options, indent=2, sort_keys=True))
