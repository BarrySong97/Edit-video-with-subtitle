function parse(srt: string) {
  srt = srt.replace(/\r/g, '');
  var regex = /(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})/g;
  let data = srt.split(regex);
  data.shift();

  var items = [];
  for (var i = 0; i < data.length; i += 4) {
    items.push({
      id: data[i].trim(),
      startTime: data[i + 1].trim(),
      endTime: data[i + 2].trim(),
      text: data[i + 3].trim(),
    });
  }

  return items;
};

export default parse;
