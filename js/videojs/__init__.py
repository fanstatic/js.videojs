from fanstatic import Library, Resource

library = Library('video.js', 'resources')

def render_shockwave_url(url):
    return '''
        <script type="text/javascript">
            videojs.options.flash.swf = '%s';
        </script>''' % url

videojs_shockwave = fanstatic.Resource(
    library, 'swf/video-js.swf', renderer=render_shockwave_url)

videojs_css = fanstatic.Resource(library, 'css/video-js.css')

videojs = fanstatic.Resource(library, 'js/video.js',
    minified='js/video.min.js',
    depends=[
        videojs_shockwave,
        videojs_css])
