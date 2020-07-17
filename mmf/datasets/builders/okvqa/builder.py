from mmf.common.registry import registry
from mmf.datasets.mmf_dataset_builder import MMFDatasetBuilder
from mmf.datasets.builders.okvqa.dataset import OKVQADataset


@registry.register_builder("okvqa")
class OKVQABuilder(MMFDatasetBuilder):
  def __init__(
      self,
      dataset_name="okvqa",
      dataset_class=OKVQADataset,
      *args,
      **kwargs,
  ):
    super().__init__(dataset_name, dataset_class, *args, **kwargs)

  @classmethod
  def config_path(cls):
    return "configs/datasets/okvqa/defaults.yaml"
