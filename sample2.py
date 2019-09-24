#!/usr/bin/env python
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Initializes a AdManagerClient using a Service Account."""

import os
import sys

from googleads import ad_manager, oauth2

def get_all_orders(client):
    # Initialize appropriate service.
    order_service = client.GetService('OrderService', version='v201908')

    # Create a statement to select orders.
    statement = ad_manager.StatementBuilder(version='v201908')

    # Retrieve a small amount of orders at a time, paging
    # through until all orders have been retrieved.
    while True:
        response = order_service.getOrdersByStatement(statement.ToStatement())
        if 'results' in response and len(response['results']):
            for order in response['results']:
                # Print out some information for each order.
                print('Order with ID "%d" and name "%s" was found.\n' % (order['id'],
                                                                         order['name']))
            statement.offset += statement.limit
        else:
            break

    print('\nNumber of results found: %s' % response['totalResultSetSize'])


def main():
    # get certificated ad manager client
    ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage('googleads.yaml')

    # get all orders
    get_all_orders(ad_manager_client)

    sys.exit(0)
    pass


if __name__ == '__main__':

    main()
