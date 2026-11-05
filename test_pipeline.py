#!/usr/bin/env python3
"""Basic tests for video pipeline."""

import unittest
from pipeline import plan_scenes, generate_subtitles, PRESETS

class TestPipeline(unittest.TestCase):
    def test_plan_scenes(self):
        scenes = plan_scenes("This is a test script for planning scenes.", 2)
        self.assertEqual(len(scenes), 2)
        self.assertIn("scene", scenes[0])

    def test_generate_subtitles(self):
        scenes = [{"text": "Hello", "duration": 3}]
        srt = generate_subtitles(scenes)
        self.assertIn("Hello", srt)

    def test_presets_exist(self):
        self.assertIn("vertical_9_16", PRESETS)

if __name__ == "__main__":
    unittest.main()
