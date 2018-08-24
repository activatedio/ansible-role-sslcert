base_directory = '/var/cache/ssl-test'


def test_ca_bundle(host):

    f = host.file('/etc/ssl/certs/consul.pem')

    assert f.exists


def test_private_directory(host):

    d = host.file(base_directory + '/private')

    assert d.exists
    assert d.is_directory
    assert d.user == 'testuser'
    assert d.group == 'testuser'
    assert d.mode == 0700


def test_certs_directory(host):

    d = host.file(base_directory + '/certs')

    assert d.exists
    assert d.is_directory
    assert d.user == 'testuser'
    assert d.group == 'testuser'
    assert d.mode == 0755


def test_key(host):

    f = host.file(base_directory + '/private/servertest.key')

    assert f.exists
    assert f.is_file
    assert f.user == 'testuser'
    assert f.group == 'testuser'
    assert f.mode == 0400


def test_cert(host):

    f = host.file(base_directory + '/certs/servertest.crt')

    assert f.exists
    assert f.is_file
    assert f.user == 'testuser'
    assert f.group == 'testuser'
    assert f.mode == 0400
