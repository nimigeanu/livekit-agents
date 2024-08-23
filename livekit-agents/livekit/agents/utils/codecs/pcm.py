from typing import List
from livekit import rtc

class PcmStreamDecoder:
    """A class to handle PCM data and convert it into AudioFrame objects."""

    def __init__(self, sample_rate: int, num_channels: int, samples_per_channel: int):
        self.sample_rate = sample_rate
        self.num_channels = num_channels
        self.samples_per_channel = samples_per_channel

    def decode_chunk(self, chunk: bytes) -> List[rtc.AudioFrame]:
        """Wraps the PCM chunk into AudioFrame objects."""
        # Since PCM is raw audio, we directly wrap it into an AudioFrame
        frame = rtc.AudioFrame(
            data=chunk,
            num_channels=self.num_channels,
            sample_rate=self.sample_rate,
            samples_per_channel=self.samples_per_channel
        )
        return [frame]
