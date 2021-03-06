import pytest


TEST_PLAYBOOKS = [
    'activation_key',
    'architecture',
    'auth_source_ldap',
    'bookmark',
    'compute_attribute',
    'compute_profile',
    'compute_resource',
    'config_group',
    'content_credential',
    'content_upload',
    'content_view',
    'content_view_filter',
    'content_view_version',
    'domain',
    'external_usergroup',
    'filters',
    'global_parameter',
    'hardware_model',
    'host',
    'host_collection',
    'host_power',
    'hostgroup',
    'http_proxy',
    'image',
    'installation_medium',
    'inventory_plugin',
    'job_template',
    'katello_hostgroup',
    'katello_manifest',
    'lifecycle_environment',
    'location',
    'luna_hostgroup',
    'operatingsystem',
    'organization',
    'os_default_template',
    'partition_table',
    'product',
    'provisioning_template',
    'puppet_environment',
    'realm',
    'redhat_manifest',
    'repository',
    'repository_set',
    'repository_sync',
    'resource_info',
    'role',
    'scap_content',
    'scap_tailoring_file',
    'setting',
    'smart_class_parameter',
    'status_info',
    'subnet',
    'sync_plan',
    'templates_import',
    'user',
    'usergroup',
]


def pytest_addoption(parser):
    parser.addoption("--record", action="store_true",
                     help="record new server-responses")


@pytest.fixture
def record(request):
    return request.config.getoption('record')
