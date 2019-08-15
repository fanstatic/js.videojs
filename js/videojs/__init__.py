from fanstatic import Library, Resource, Group

library = Library('video.js', 'resources')

# By default, we bundle Video.js with Mozilla's excellent VTT.js.
videojs_js = Resource(
    library, 'video.js', minified='video.min.js')

# If you don't need VTT.js functionality for whatever reason, you can use one
# of the Video.js copies that don't include VTT.js.
videojs_js_novtt = Resource(
    library, 'alt/video.novtt.js', minified='alt/video.novtt.min.js')

# Video.js will be bundling VHS by default for ease of use for new users.
# However, some people don’t want VHS or are using another plugin.
# For this, we have a separate build of Video.js which doesn’t include VHS.
# https://blog.videojs.com/introducing-video-js-http-streaming-vhs/
videojs_core_js = Resource(
    library, 'alt/video.core.js', minified='alt/video.core.min.js')

videojs_core_js_novtt = Resource(
    library, 'alt/video.core.novtt.js', minified='alt/video.core.novtt.min.js')

videojs_css = Resource(library, 'video-js.css', minified='video-js.min.css')

videojs = Group(depends=[videojs_js, videojs_css])

videojs_novtt = Group(
    depends=[
        videojs_js_novtt,
        videojs_css])

videojs_core = Group(depends=[videojs_core_js, videojs_css])

videojs_core_novtt = Group(
    depends=[
        videojs_core_js_novtt,
        videojs_css])
