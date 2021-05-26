#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The eos_prefix_lists config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

import q
from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.resource_module import (
    ResourceModule,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.facts.facts import (
    Facts,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.rm_templates.prefix_lists import (
    Prefix_listsTemplate,
)


class Prefix_lists(ResourceModule):
    """
    The eos_prefix_lists config class
    """

    def __init__(self, module):
        super(Prefix_lists, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="prefix_lists",
            tmplt=Prefix_listsTemplate(),
        )
        self.parsers = []

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """ Generate configuration commands to send based on
            want, have and desired state.
        """
        wantd = {entry["afi"]: entry for entry in self.want}
        haved = {entry["afi"]: entry for entry in self.have}

        # turn all lists of dicts into dicts prior to merge
        q("START", wantd, haved)
        for entry in wantd, haved:
            self._prefix_lists_list_to_dict(entry)

        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(haved, wantd)

        # if state is deleted, empty out wantd and set haved to wantd
        if self.state == "deleted":
            haved = {
                k: v for k, v in iteritems(haved) if k in wantd or not wantd
            }
            wantd = {}

        # remove superfluous config for overridden and deleted
        if self.state in ["overridden", "deleted"]:
            for k, have in iteritems(haved):
                if k not in wantd:
                    self._compare(want={}, have=have)
        q(wantd, haved)
        for k, want in iteritems(wantd):
            self._compare(want=want, have=haved.pop(k, {}))

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Prefix_lists network resource.
        """
        self.compare(parsers=self.parsers, want=want, have=have)

    def _prefix_lists_list_to_dict(self, entry):
        for afi, plist in iteritems(entry):
            q("enter", afi, plist)
            if "prefix_lists" in plist:
                pl_dict = {}
                for el in plist["prefix_lists"]:
                    if "entries" in el:
                        ent_dict = {}
                        for en in el["entries"]:
                            if not "sequence" in en:
                                num = "seq"
                            else:
                                num = en["sequence"]
                            ent_dict.update({num: en})
                        el["entries"] = ent_dict
                for el in plist["prefix_lists"]:
                    pl_dict.update({el["name"]: el})
                plist["prefix_lists"] = pl_dict
            # entry[afi] = plist
        q("OUT", entry)
