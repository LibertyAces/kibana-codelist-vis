FROM docker.elastic.co/kibana/kibana:6.4.2
COPY ./build/kibana_codelist_vis-18.08.03.zip /kibana_codelist_vis-18.08.03.zip
RUN ./bin/kibana-plugin install file:///kibana_codelist_vis-18.08.03.zip
