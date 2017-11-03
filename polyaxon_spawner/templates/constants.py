# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from polyaxon_schemas.polyaxonfile import constants

K8S_API_VERSION_V1 = 'v1'
K8S_API_VERSION_V1_BETA1 = 'extensions/v1beta1'
K8S_PERSISTENT_VOLUME_KIND = 'PersistentVolume'
K8S_PERSISTENT_VOLUME_CLAIM_KIND = 'PersistentVolumeClaim'
K8S_CONFIG_MAP_KIND = 'ConfigMap'
K8S_POD_KIND = 'Pod'
K8S_POD_TEMPLATE_KIND = 'PodTemplate'
K8S_DEPLOYMENT_KIND = 'Deployment'
K8S_SERVICE_KIND = 'Service'
K8S_INGRESS_KIND = 'Ingress'
DOCKER_IMAGE = 'polyaxon/polyaxon:lib-cpu-3-121'
ENV_VAR_TEMPLATE = '{name: "{var_name}", value: "{var_value}"}'
VOLUME_NAME = 'pv-{project}-{vol_name}'
VOLUME_CLAIM_NAME = 'pvc-{project}-{vol_name}'
GPU_RESOURCES = '{alpha.kubernetes.io/nvidia-gpu: {}'
CONFIG_MAP_CLUSTER_NAME = '{project}-xp{experiment}-cluster'
CONFIG_MAP_CLUSTER_KEY_NAME = 'CM_{project}_xp{experiment}_cluster_{task_type}'
TASK_LABELS = ('project: "{project}", '
               'experiment: "{experiment}", '
               'task_type: "{task_type}", '
               'task_id: "{task_id}", '
               'task: "{task_name}"')
POD_CONTAINER_TASK_NAME = '{project}-xp{experiment}-{task_type}{task_id}'
POD_CONTAINER_PROJECT_NAME = '{project}-{name}'
DEPLOYMENT_NAME = '{project}-{name}'


DATA_VOLUME = constants.DATA_VOLUME
LOGS_VOLUME = constants.LOGS_VOLUME
POLYAXON_FILES_VOLUME = constants.POLYAXON_FILES_VOLUME
TASK_NAME = constants.TASK_NAME
DEFAULT_PORT = constants.DEFAULT_PORT