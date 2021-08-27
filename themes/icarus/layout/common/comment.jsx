const logger = require('hexo-log')();
const { Component } = require('inferno');
const view = require('hexo-component-inferno/lib/core/view');

module.exports = class extends Component {
    render() {
        const { config, page, helper } = this.props;
        const { __ } = helper;
        const { comment } = config;
        if (!comment || typeof comment.type !== 'string') {
            return null;
        }

        return <div class="card">

            <div class="card-content">
                <h3 class="title is-5">{__('article.comments')}</h3>
                {(() => {
                    try {
                        let Comment = view.require('comment/' + comment.type);
                        Comment = Comment.Cacheable ? Comment.Cacheable : Comment;
                        return <Comment config={config} page={page} helper={helper} comment={comment} />;
                    } catch (e) {
                        logger.w(`Icarus cannot load comment "${comment.type}"`);
                        return null;
                    }
                })()}
            </div>
            <span styl="max-width: 95%">
            <script src="https://giscus.app/client.js"
                    data-repo="karobben/utterances"
                    data-repo-id="MDEwOlJlcG9zaXRvcnkyNzUwNjUwODg="
                    data-category="Announcements"
                    data-category-id="DIC_kwDOEGUpAM4B-wRL"
                    data-mapping="pathname"
                    data-reactions-enabled="1"
                    data-emit-metadata="0"
                    data-theme="light"
                    crossorigin="anonymous"
                    async>
            </script>
            </span>
        </div>;
    }
};
