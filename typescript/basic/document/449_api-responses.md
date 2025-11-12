# #449 「レスポンス」

四国めたん「voidレスポンスではHTTPステータスを明確に選びましょう。」
ずんだもん「204 No Contentが推奨されてたね。」
四国めたん「非同期処理なら202 Acceptedも活用できます。」
ずんだもん「updateのように200 OKでもボディなしで返せるんだ?」
四国めたん「はい。必要に応じて適切なステータスを選んでください。」
ずんだもん「void戻り値と組み合わせればAPIの振る舞いが読みやすい!」
四国めたん「クライアントとの契約としても重要です。」
ずんだもん「ステータス設計でvoidレスポンスを使いこなすのだ!」

---

## 📺 画面表示用コード

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
