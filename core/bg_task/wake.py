import pvporcupine
import pyaudio
import struct
import json
from sanic import Sanic



class PorcupineListener:
    def __init__(self):
        self.porcupine = pvporcupine.create(access_key='vHB6XClX1oLPDNz6xFODSgswQ5X4++5Zqgy7PbLihnaZgSYEJW1rAA==',keyword_paths=['/Users/solo/code/wall-E/core/bg_task/hello.ppn'])

        self.audio_stream = pyaudio.PyAudio().open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length)

    async def run(self):
        try:
            print("后台任务开始运行，正在监听唤醒词")
            while True:
                pcm = self.audio_stream.read(self.porcupine.frame_length)
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)

                keyword_index = self.porcupine.process(pcm)

                if keyword_index >= 0:
                        print("监听到【唤醒词】")
                        # app = Sanic.get_app()
                        # await app.dispatch('task.wake.happened')
                        break
                    # else:
                #     print("我在听")

        except KeyboardInterrupt:
            print('Interrupted by user')
        finally:
            if self.audio_stream is not None:
                self.audio_stream.close()

            if self.porcupine is not None:
                self.porcupine.delete()

# if __name__ == '__main__':
#     listener = PorcupineListener()
#     listener.run()
