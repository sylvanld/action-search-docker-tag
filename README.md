# Search Docker tag action

Search for last docker tag matching given pattern.

## Inputs

## `image`

**Required** Full name of the image (as in: example/image, library/redis)

## `search`

**Optional** A python regex pattern that searched tag must match.

Defaults to `.+` meaning "match any version".

## Outputs

## `tag`

The latest tag matching your search.

## Example usage

```yaml
jobs:
  example_job:
    ...
    steps:
      - name: "Get latest redis tag"
        id: get-redis-tag
        uses: sylvanld/action-search-docker-tag@v1
        with:
          image: 'library/redis'
          search: '\d+\.\d+\.\d+'

      - name: "Get the output time"
        run: echo "Redis latest version -> ${{ steps.get-redis-tag.outputs.tag }}"
```
