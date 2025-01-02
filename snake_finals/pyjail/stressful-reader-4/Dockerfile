# use the jail base image
FROM ghcr.io/madrhacks/jail:latest
# copy the root files from any Docker image
COPY --from=python@sha256:59c7332a4a24373861c4a5f0eec2c92b87e3efeb8ddef011744ef9a751b1d11c / /srv
# setup the binary to run
RUN mkdir /srv/app
COPY chall /srv/app/run

ENV FLAG_PATH=/app/flag.txt

ENTRYPOINT [ "tail", "-f", "/dev/null" ]
