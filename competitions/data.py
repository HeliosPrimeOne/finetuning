from dataclasses import dataclass, field
from enum import IntEnum
from typing import Any, List, Optional, Type

from transformers import PreTrainedModel


class CompetitionId(IntEnum):
    """Unique identifiers for each competition."""

    SN9_MODEL = 1
    
    # Defined for tests. Will be repurposed later.
    COMPETITION_2 = 2


@dataclass
class ModelConstraints:
    """Defines the constraints for models submitted to a specific competition."""
    # The maximum parameter size allowed for models
    max_model_parameter_size: int
    
    # Architecture class of model
    allowed_architectures: List[Type[PreTrainedModel]]
    
    # The list of tokenizers allowed. If none, any tokenizer can be used.
    allowed_tokenizers: Optional[List[str]] = None
    
    # The model's sequence length.
    sequence_length: int
    
    # Any additional arguments to pass to from_pretrained
    kwargs: Any = field(default_factory=dict)


@dataclass
class Competition:
    """Defines a competition."""
    
    # Unique ID for this competition.
    id: CompetitionId
    
    # All restrictions on models allowed in this competition.
    constraints: ModelConstraints
    
    # Percentage of emissions dedicated to this competition.
    reward_percentage: float
