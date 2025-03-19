# Copyright (C) 2015, Wazuh Inc.
# Created by Wazuh, Inc. <info@wazuh.com>.
# This program is a free software; you can redistribute it and/or modify it under the terms of GPLv2


import asyncio

import pytest
from uvloop import EventLoopPolicy, Loop
from wazuh.core.config.client import Config
from wazuh.core.config.models.indexer import IndexerConfig, IndexerNode
from wazuh.core.config.models.server import NodeConfig, NodeType, ServerConfig, SSLConfig


def get_default_configuration():
    """Get default configuration for the tests."""
    return Config(
        server=ServerConfig(
            nodes=['0'],
            node=NodeConfig(
                name='node_name',
                type=NodeType.MASTER,
                ssl=SSLConfig(key='example', cert='example', ca='example'),
            ),
        ),
        indexer=IndexerConfig(hosts=[IndexerNode(host='example', port=1516)], username='wazuh', password='wazuh'),
    )


@pytest.fixture(scope='session')
def event_loop() -> Loop:
    asyncio.set_event_loop_policy(EventLoopPolicy())
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()
