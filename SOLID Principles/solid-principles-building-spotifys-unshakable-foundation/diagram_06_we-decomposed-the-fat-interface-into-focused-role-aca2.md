# We decomposed the fat interface into focused role 

```mermaid
---
config:
  layout: elk
  theme: base
---
classDiagram
    class IPlayable {
        <<interface>>
        +PlayAsync()
        +PauseAsync()
        +StopAsync()
    }
    
    class IDownloadable {
        <<interface>>
        +DownloadAsync()
        +DeleteDownloadAsync()
    }
    
    class IShareable {
        <<interface>>
        +ShareAsync()
    }
    
    class IAnalyticsTrackable {
        <<interface>>
        +TrackPlayAsync()
    }
    
    class IPlaylistManageable {
        <<interface>>
        +AddToPlaylistAsync()
    }
    
    class Song {
        +IPlayable
        +IDownloadable
        +IShareable
        +IAnalyticsTrackable
    }
    
    class Podcast {
        +IPlayable
        +IDownloadable
        +IShareable
        +IAnalyticsTrackable
    }
    
    class Ad {
        +IPlayable
        +IAnalyticsTrackable
    }
    
    IPlayable <|.. Song
    IPlayable <|.. Podcast
    IPlayable <|.. Ad
    IDownloadable <|.. Song
    IDownloadable <|.. Podcast
    IShareable <|.. Song
    IShareable <|.. Podcast
    IAnalyticsTrackable <|.. Song
    IAnalyticsTrackable <|.. Podcast
    IAnalyticsTrackable <|.. Ad
```
