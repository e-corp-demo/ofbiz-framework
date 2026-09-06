#!/usr/bin/env sh
set -eu

sed -i \
  -e 's#^port.https=.*#port.https=18443#' \
  -e 's#^force.https.host=.*#force.https.host=localhost#' \
  -e 's#^content.url.prefix.secure=.*#content.url.prefix.secure=https://localhost:18443#' \
  -e 's#^content.url.prefix.standard=.*#content.url.prefix.standard=https://localhost:18443#' \
  /ofbiz/config/url.properties
