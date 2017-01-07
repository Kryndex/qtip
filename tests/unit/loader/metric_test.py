###############################################################
# Copyright (c) 2016 ZTE Corp and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

import pytest

from qtip.base.benchmark import Property
from qtip.spec.metric import MetricSpec


@pytest.fixture(scope='module')
def metric_spec(benchmarks_root):
    return MetricSpec('dhrystone.yaml', paths=[benchmarks_root])


def init_test(metric_spec):
    assert metric_spec.name == 'dhrystone'

    with pytest.raises(TypeError) as excinfo:
        MetricSpec()
    assert '__init__() takes at least 2 arguments (1 given)' \
           in str(excinfo.value)


def list_all_test():
    metric_list = MetricSpec.list_all()
    assert len(list(metric_list)) is 1
    for desc in metric_list:
        assert Property.NAME in desc
        assert Property.DESCRIPTION in desc
        assert Property.ABSPATH in desc
        assert Property.ABSPATH is not None


def content_test(metric):
    content = metric.content()
    assert Property.NAME in content
    assert Property.DESCRIPTION in content
    assert Property.WORKLOADS in content
    assert isinstance(content[Property.WORKLOADS], list)