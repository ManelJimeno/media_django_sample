# Media file 

We need to define an API for our media platform that organizes content in a hierarchical structure.

Each piece of content can include files (e.g., videos, PDFs, or text), metadata (such as descriptions,
authors, and genres), and a rating between 0 and 10.

Content is managed through Channels, which define the hierarchy. A channel has a title, language,
and image, and it can either contain subchannels or content, but never both. Each channel must have at
least one subchannel or one content item.

A channel’s rating is calculated dynamically as the average rating of its subchannels or, if it has
none, the average of its contents. Channels without content do not contribute to their parent’s rating.
Since the structure is dynamic, ratings cannot be stored directly and must be computed as needed.
