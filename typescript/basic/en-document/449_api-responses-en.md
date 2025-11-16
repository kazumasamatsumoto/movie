# #449 "Responses"

Shikoku Metan: "Pick precise HTTP statuses for void responses."
Zundamon: "204 No Content was recommended."
Shikoku Metan: "For async work, 202 Accepted fits."
Zundamon: "update still returned 200 OK with an empty body."
Shikoku Metan: "Choose the status that matches the behavior."
Zundamon: "Combined with void returns, APIs stay predictable."
Shikoku Metan: "It reinforces the contract with clients."
Zundamon: "I'll master status design for void responses!"

---

## 📺 Code for Display

```typescript
/** Example 1: 204 No Content */
@Delete(':id')
@HttpCode(204)
async delete(@Param('id') id: string): Promise<void> {
  await this.service.delete(id);
}

/** Example 2: 202 Accepted */
@Post('process')
@HttpCode(202)
async process(@Body() dto: ProcessDto): Promise<void> {
  await this.queue.add(dto);
}

/** Example 3: 200 OK */
@Put(':id')
async update(@Param('id') id: string, @Body() dto: UpdateDto): Promise<void> {
  await this.service.update(id, dto);
}
```
