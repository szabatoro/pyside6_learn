import pyalpm

# Initialize pyalpm
handle = pyalpm.Handle("/", "/var/lib/pacman")

# Set up pacman dbs
core_db = handle.register_syncdb("core", pyalpm.SIG_DATABASE_OPTIONAL)
extra_db = handle.register_syncdb("extra", pyalpm.SIG_DATABASE_OPTIONAL)
multilib_db = handle.register_syncdb("multilib", pyalpm.SIG_DATABASE_OPTIONAL)
syncdbs = handle.get_syncdbs()

localdb = handle.get_localdb()
installed_pkgs = localdb.search("")

def fetch_updates():
    updates = []
    for db in syncdbs:
        for pkg in installed_pkgs:
            candidate = db.get_pkg(pkg.name)
            if candidate and pyalpm.vercmp(candidate.version, pkg.version) > 0:
                updates.append((pkg.name, pkg.version, candidate.version, db.name))

    return updates

def fetch_all_packages():
    packages = []
    for db in syncdbs:
        for pkg in db.pkgcache:
            packages.append((pkg.name, pkg.version, db.name))
    return packages