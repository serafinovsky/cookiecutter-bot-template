DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '{{cookiecutter.project_slug}}') THEN
        CREATE USER {{cookiecutter.project_slug}} WITH PASSWORD '{{cookiecutter.project_slug}}' CREATEDB;
    END IF;

    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = '{{cookiecutter.project_slug}}') THEN
        CREATE DATABASE {{cookiecutter.project_slug}} WITH OWNER = {{cookiecutter.project_slug}};
    END IF;
END
$$;